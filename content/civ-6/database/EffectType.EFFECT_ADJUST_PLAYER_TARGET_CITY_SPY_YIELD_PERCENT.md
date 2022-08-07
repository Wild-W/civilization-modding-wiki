---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TARGET_CITY_SPY_YIELD_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TARGET_CITY_SPY_YIELD_PERCENT
>
> * Class: `Unknown`
> * Parameters:
>	* Percent `Unknown`
>	* YieldType `Unknown`

## Samples
```SQL {title="GOVERNOR_PROMOTION_OWLS_OF_MINERVA_4_SPY_SUCCESS_GRANTS_SCIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOVERNOR_PROMOTION_OWLS_OF_MINERVA_4_SPY_SUCCESS_GRANTS_SCIENCE",
		"MODIFIER_PLAYER_ADJUST_TARGET_CITY_SPY_YIELD_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOVERNOR_PROMOTION_OWLS_OF_MINERVA_4_SPY_SUCCESS_GRANTS_SCIENCE",
		"Percent",
		50
	),
	(
		"GOVERNOR_PROMOTION_OWLS_OF_MINERVA_4_SPY_SUCCESS_GRANTS_SCIENCE",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

