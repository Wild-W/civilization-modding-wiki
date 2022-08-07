---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_POST_COMBAT_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_POST_COMBAT_YIELD
>
> * Class: `UNITS`
> * Parameters:
>	* OnlyWhenDefeatedEarlierEraUnit `Boolean`
>	* PercentDefeatedStrength `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="NATIVECONQUEST_ADJUSTPOSTCOMBATYIELD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"NATIVECONQUEST_ADJUSTPOSTCOMBATYIELD",
		"MODIFIER_PLAYER_UNITS_ADJUST_POST_COMBAT_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NATIVECONQUEST_ADJUSTPOSTCOMBATYIELD",
		"OnlyWhenDefeatedEarlierEraUnit",
		1
	),
	(
		"NATIVECONQUEST_ADJUSTPOSTCOMBATYIELD",
		"PercentDefeatedStrength",
		50
	),
	(
		"NATIVECONQUEST_ADJUSTPOSTCOMBATYIELD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

```SQL {title="GOD_OF_WAR_FAITH_KILLS_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"GOD_OF_WAR_FAITH_KILLS_MODIFIER",
		"MODIFIER_PLAYER_UNITS_ADJUST_POST_COMBAT_YIELD",
		"PLOT_EIGHT_INCLUDE_HOLY_SITE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOD_OF_WAR_FAITH_KILLS_MODIFIER",
		"PercentDefeatedStrength",
		50
	),
	(
		"GOD_OF_WAR_FAITH_KILLS_MODIFIER",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

