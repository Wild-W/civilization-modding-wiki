---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_PROPERTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_PROPERTY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Unknown`
>	* Key `Unknown`

## Samples
```SQL {title="MODIFIER_SHRINE_CITY_HERO_EXTRA_LIFESPAN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MODIFIER_SHRINE_CITY_HERO_EXTRA_LIFESPAN",
		"MODIFIER_SINGLE_CITY_ADJUST_PROPERTY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MODIFIER_SHRINE_CITY_HERO_EXTRA_LIFESPAN",
		"Amount",
		10
	),
	(
		"MODIFIER_SHRINE_CITY_HERO_EXTRA_LIFESPAN",
		"Key",
		"CityHeroExtraLifespan"
	);
	
```

