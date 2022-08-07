---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_GREATWORK_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_GREATWORK_YIELD
>
> * Class: `CITIES`
> * Parameters:
>	* GreatWorkObjectType `String`
>		* [GreatWorkObjectTypes.GreatWorkObjectType]
>	* ScalingFactor `Integer`
>	* YieldChange `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="RELIQUARIES_RELIC_FAITH_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"RELIQUARIES_RELIC_FAITH_MODIFIER",
		"MODIFIER_SINGLE_CITY_ADJUST_GREATWORK_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RELIQUARIES_RELIC_FAITH_MODIFIER",
		"GreatWorkObjectType",
		"GREATWORKOBJECT_RELIC"
	),
	(
		"RELIQUARIES_RELIC_FAITH_MODIFIER",
		"ScalingFactor",
		300
	),
	(
		"RELIQUARIES_RELIC_FAITH_MODIFIER",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

```SQL {title="TRAIT_GREAT_WORK_FAITH_SCULPTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_GREAT_WORK_FAITH_SCULPTURE",
		"MODIFIER_PLAYER_CITIES_ADJUST_GREATWORK_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_GREAT_WORK_FAITH_SCULPTURE",
		"GreatWorkObjectType",
		"GREATWORKOBJECT_SCULPTURE"
	),
	(
		"TRAIT_GREAT_WORK_FAITH_SCULPTURE",
		"YieldChange",
		1
	),
	(
		"TRAIT_GREAT_WORK_FAITH_SCULPTURE",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

