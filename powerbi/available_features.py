from typing import Dict
from powerbi.session import PowerBiSession


class AvailableFeatures():

    def __init__(self, session: object) -> None:
        """Initializes the `AvailableFeatures` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> available_features_service = power_bi_client.available_features()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    def get_available_features(self) -> Dict:
        """Returns a list of available features for the user.

        ### Returns
        ----
        Dict
            A collection of `AvailableFeature` resources.

        ### Usage
        ----
            >>> available_features_service = power_bi_client.available_features()
            >>> available_features_service.get_available_features()
        """

        # Make the request.
        content = self.power_bi_session.make_request(
            method='get',
            endpoint='myorg/availableFeatures'
        )

        return content

    def get_available_feature_by_name(self, feature_name: str) -> Dict:
        """Returns the specified available feature for user by name.

        ### Parameters
        ----
        str :
            The feature name.

        ### Returns
        ----
        Dict
            A `AvailableFeature` resource.

        ### Usage
        ----
            >>> available_features_service = power_bi_client.available_features()
            >>> available_features_service.get_available_featureby_name(
                feature_name='embedTrial'
            )
        """

        # Make the request.
        content = self.power_bi_session.make_request(
            method='get',
            endpoint="myorg/availableFeatures(featureName='" +
            feature_name + "')"
        )

        return content
