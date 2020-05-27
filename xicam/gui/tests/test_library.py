from pytest import fixture
import pytest
from pytestqt import qtbot
import event_model
import numpy as np
import time
from databroker.in_memory import BlueskyInMemoryCatalog
from xicam.gui.widgets.library import LibraryWidget, LibraryView
from qtpy.QtWidgets import QWidget, QHBoxLayout, QSlider
from functools import partial

data_shape = (100, 100)
frames = 100


def doc_stream(streams, fields):
    def doc_gen(stream_names):

        # Compose run start
        run_bundle = event_model.compose_run()  # type: event_model.ComposeRunBundle
        start_doc = run_bundle.start_doc

        yield 'start', start_doc

        for stream_name in stream_names:

            data = np.random.random(data_shape)

            # Compose descriptor
            source = 'NCEM'
            frame_data_keys = {field: {'source': source,
                                       'dtype': 'number',
                                       'shape': data.shape} for field in fields}
            frame_stream_bundle = run_bundle.compose_descriptor(data_keys=frame_data_keys,
                                                                name=stream_name,
                                                                )
            yield 'descriptor', frame_stream_bundle.descriptor_doc

            yield 'event', frame_stream_bundle.compose_event(data={field: data for field in fields},
                                                             timestamps={field: time.time() for field in fields})

        yield 'stop', run_bundle.compose_stop()
    return doc_gen(streams)


@fixture
def random_data_catalog(request):
    N = request.param
    catalog = BlueskyInMemoryCatalog()

    for i in range(N):
        docs = list(doc_stream(streams=["primary", "baseline"], fields=["cam1", "cam2"]))
        start = docs[0][1]
        stop = docs[-1][1]

        def doc_gen():
            yield from docs

        catalog.upsert(start, stop, doc_gen, [], {})

    return catalog


# def test_library_widget(qtbot):
#
#     w = QWidget()
#     w.setLayout(QHBoxLayout())
#
#     l = LibraryWidget()
#     for i in range(15):
#         l.add_image(np.random.random((1000, 1000)), "Sample {i+1}")
#
#     s = QSlider()
#     s.valueChanged.connect(partial(l.set_slice, axis="E"))
#
#     w.layout().addWidget(l)
#     w.layout().addWidget(s)
#
#     w.show()
#
#     qtbot.addWidget(w)
#     qtbot.stopForInteraction()


@pytest.mark.parametrize("random_data_catalog", (1,), indirect=True)
def test_catalog(random_data_catalog):
    assert random_data_catalog[-1].primary.to_dask()['cam1'].compute() is not None


@pytest.mark.parametrize("random_data_catalog", (10,), indirect=True)
def test_library_view(qtbot, random_data_catalog):
    from xicam.plugins.catalogplugin import CatalogModel
    model = CatalogModel(random_data_catalog)

    w = QWidget()
    w.setLayout(QHBoxLayout())

    l = LibraryView(model)

    s = QSlider()
    s.valueChanged.connect(partial(l.set_slice, axis="E"))

    w.layout().addWidget(l)
    w.layout().addWidget(s)

    w.show()

    qtbot.addWidget(w)
    qtbot.stopForInteraction()

