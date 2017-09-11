from .decorators import endpoint
from ..endpoints.account import *
from ..endpoints.annotations import *


class AccountInterface(object):


    @endpoint(GETAccounts)
    def list_accounts(self):
        """
        Get a list of all Accounts authorized for the provided token.

        Args:

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountID)
    def get_accounts(self):
        """
        Get the full details for a single Account that a client has access to.
        Full pending Order, open Trade and open Position representations are
        provided.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountIDSummary)
    def account_summary(self):
        """
        Get a summary for a single Account that a client has access to.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountIDInstruments)
    def account_instruments(self, instruments: Instruments):
        """
        Get the list of tradeable instruments for the given Account. The list
        of tradeable instruments is dependent on the regulatory division that
        the Account is located in, thus should be the same for all Accounts
        owned by a single user.

        Args:
            accountID:
                Account Identifier
            instruments:
                List of instruments to query specifically.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass


    @endpoint(PATCHAccountIDConfiguration)
    def configure_account(self, alias: Alias, marginRate: DecimalNumber):
        """
        Set the client-configurable portions of an Account.

        Args:
            accountID:
                Account Identifier
            alias:
                Client-defined alias (name) for the Account
            marginRate:
                The string representation of a decimal number.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountIDChanges)
    def account_changes(self, sinceTransactionID: TransactionID):
        """
        Endpoint used to poll an Account for its current state and changes
        since a specified TransactionID.

        Args:
            accountID:
                Account Identifier
            sinceTransactionID:
                ID of the Transaction to get Account changes since.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass