---
tags:
- EffectType
title: EFFECT_GRANT_RANDOM_TECHNOLOGY_BOOST_BY_ERA
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_RANDOM_TECHNOLOGY_BOOST_BY_ERA
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* EndEraType `String`
>		* [Eras.EraType]
>	* StartEraType `String`
>		* [Eras.EraType]

## Samples

```SQL {title="GREATPERSON_1MODERNTECHBOOST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_1MODERNTECHBOOST",
		"MODIFIER_PLAYER_GRANT_RANDOM_TECHNOLOGY_BOOST_BY_ERA",
		1,
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
		"GREATPERSON_1MODERNTECHBOOST",
		"Amount",
		1
	),
	(
		"GREATPERSON_1MODERNTECHBOOST",
		"EndEraType",
		"ERA_MODERN"
	),
	(
		"GREATPERSON_1MODERNTECHBOOST",
		"StartEraType",
		"ERA_MODERN"
	);
	
```

