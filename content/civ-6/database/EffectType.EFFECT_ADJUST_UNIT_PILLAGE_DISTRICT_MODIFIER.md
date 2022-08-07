---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_PILLAGE_DISTRICT_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_PILLAGE_DISTRICT_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="SACK_DOUBLEPILLAGEDISTRICT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SACK_DOUBLEPILLAGEDISTRICT",
		"MODIFIER_PLAYER_ADJUST_DISTRICT_PILLAGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value,
		Extra
	)
VALUES
	(
		"SACK_DOUBLEPILLAGEDISTRICT",
		"Amount",
		50,
		"-1"
	);
	
```

