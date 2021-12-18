

class ImportBuilder():

    def __init__(self, file_type: str) -> None:

        self.allowed_file_types = [
            'xlsx',
            'json',
            'pbix',
            'rdl',
            'onedrive'
        ]

        if file_type not in self.allowed_file_types:
            raise ValueError(
                "File type not supported, please provide file types that are supported."
            )

        _content_header = f"""
        Content-Disposition: form-data; filename="{0}"
        Content-Type: {0}
        """

    def set_file_type(self) -> None:
        pass

    def set_file_path(self) -> None:
        pass

    def load_and_encode(self, file_path: str) -> None:
        pass

    def connection_details(self, connection_type: str = None, file_path: str = None, file_url: str = None) -> None:
        pass

    def _construct_headers(self) -> None:
        pass

    def _validate_file_extension(self) -> None:
        pass
