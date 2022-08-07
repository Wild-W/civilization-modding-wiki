---
tags:
- EffectType
title: EFFECT_ADJUST_GOVERNOR_ALLIANCE_POINTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GOVERNOR_ALLIANCE_POINTS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="KHASS_ODA_BASHI_ADJUST_ALLIANCE_POINTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"KHASS_ODA_BASHI_ADJUST_ALLIANCE_POINTS",
		"MODIFIER_GOVERNOR_ADJUST_ALLIANCE_POINTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"KHASS_ODA_BASHI_ADJUST_ALLIANCE_POINTS",
		"Amount",
		2
	);
	
```

