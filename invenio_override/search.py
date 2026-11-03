# SPDX-FileCopyrightText: 2020-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Frontpage records."""

from invenio_search.api import RecordsSearch

try:
    from invenio_global_search import __version__

    DEFAULT_INDEX = "global-search"
except ImportError:
    DEFAULT_INDEX = "rdmrecords-records"


class FrontpageRecordsSearch(RecordsSearch):
    """Search class for records that goes on the frontpage."""

    class Meta:
        """Default index and filter for frontpage search."""

        index = DEFAULT_INDEX
