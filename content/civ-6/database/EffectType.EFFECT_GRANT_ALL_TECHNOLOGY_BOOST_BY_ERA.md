---
tags:
- EffectType
title: EFFECT_GRANT_ALL_TECHNOLOGY_BOOST_BY_ERA
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_ALL_TECHNOLOGY_BOOST_BY_ERA
>
> * Class: `PLAYERS`
> * Parameters:
>	* EndEraType `String`
>		* [Eras.EraType]
>	* StartEraType `String`
>		* [Eras.EraType]

## Samples

```SQL {title="GREAT_LIBRARY_ANCIENT_CLASSICAL_TECH_BOOSTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREAT_LIBRARY_ANCIENT_CLASSICAL_TECH_BOOSTS",
		"MODIFIER_PLAYER_GRANT_ALL_TECHNOLOGY_BOOST_BY_ERA",
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
		"GREAT_LIBRARY_ANCIENT_CLASSICAL_TECH_BOOSTS",
		"EndEraType",
		"ERA_CLASSICAL"
	),
	(
		"GREAT_LIBRARY_ANCIENT_CLASSICAL_TECH_BOOSTS",
		"StartEraType",
		"ERA_ANCIENT"
	);
	
```

