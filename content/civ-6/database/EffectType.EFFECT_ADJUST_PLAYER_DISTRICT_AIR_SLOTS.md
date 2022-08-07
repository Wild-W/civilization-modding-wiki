---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_DISTRICT_AIR_SLOTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_DISTRICT_AIR_SLOTS
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="HANGAR_BONUS_AIR_SLOTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		Permanent
	)
VALUES
	(
		"HANGAR_BONUS_AIR_SLOTS",
		"MODIFIER_PLAYER_DISTRICT_GRANT_AIR_SLOTS",
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HANGAR_BONUS_AIR_SLOTS",
		"Amount",
		1
	);
	
```

