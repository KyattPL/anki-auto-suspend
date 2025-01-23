from aqt import (
    mw,
    gui_hooks
)
from aqt.utils import tooltip, showInfo, qconnect
from aqt.operations.scheduling import suspend_cards
import aqt
config = aqt.mw.addonManager.getConfig(__name__)

def check_cards_coll(coll):
    cardIds = mw.col.find_cards(f"prop:ivl>={config['suspend_point']}")

    cards = []
    for id in cardIds:
        card = mw.col.get_card(id)
        card.queue = -1
        cards.append(card)
    
    mw.col.update_cards(cards)


action = aqt.qt.QAction("Auto suspend cards", mw)
qconnect(action.triggered, check_cards_coll)
mw.form.menuTools.addAction(action)

gui_hooks.collection_did_load.append(check_cards_coll)