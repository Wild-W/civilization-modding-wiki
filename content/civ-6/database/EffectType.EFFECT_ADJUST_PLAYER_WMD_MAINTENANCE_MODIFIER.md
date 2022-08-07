---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_WMD_MAINTENANCE_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_WMD_MAINTENANCE_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="SECONDSTRIKE_MAINTENANCEWMDS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SECONDSTRIKE_MAINTENANCEWMDS",
		"MODIFIER_PLAYER_ADJUST_WMD_MAINTENANCE_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SECONDSTRIKE_MAINTENANCEWMDS",
		"Amount",
		50
	);
	
```

