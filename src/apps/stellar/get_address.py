from apps.common import seed
from apps.common.display_address import show_address, show_qr
from apps.stellar import helpers
from trezor.messages.StellarAddress import StellarAddress
from trezor.messages.StellarGetAddress import StellarGetAddress


async def get_address(ctx, msg: StellarGetAddress):
    node = await seed.derive_node(ctx, msg.address_n, helpers.STELLAR_CURVE)
    pubkey = seed.remove_ed25519_public_key_prefix(node.public_key())  # todo better?
    address = helpers.address_from_public_key(pubkey)

    if msg.show_display:
        while True:
            if await show_address(ctx, address):
                break
            if await show_qr(ctx, address.upper()):
                break

    return StellarAddress(address=address)