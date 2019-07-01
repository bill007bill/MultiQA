
class MultiQA_DataSet():
    """
       A ``DatasetReader`` knows how to turn a file containing a dataset into a collection
       of ``Instance`` s.  To implement your own, just override the `_read(file_path)` method
       to return an ``Iterable`` of the instances. This could be a list containing the instances
       or a lazy generator that returns them one at a time.

       All parameters necessary to _read the data apart from the filepath should be passed
       to the constructor of the ``DatasetReader``.

       Parameters
       ----------
       lazy : ``bool``, optional (default=False)
           If this is true, ``instances()`` will return an object whose ``__iter__`` method
           reloads the dataset each time it's called. Otherwise, ``instances()`` returns a list.
       """

    def __init__(self):
        pass

    def get_multiqa_version(self):
        return '0.00'

    def compute_schema(self, contexts):
        return {}

    def build_contexts(self):
        pass

    def build_header(self):
        pass