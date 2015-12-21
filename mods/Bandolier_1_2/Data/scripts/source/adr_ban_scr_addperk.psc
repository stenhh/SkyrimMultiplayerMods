Scriptname aDr_BAN_scr_addPerk extends ObjectReference  
{Adds perk to player}

Perk Property Dr_BAN_perk auto

Event OnRead(Actor akActor)
  //Debug.Notification("Perk Added")
  Game.GetPlayer().addPerk(Dr_BAN_perk)
endEvent