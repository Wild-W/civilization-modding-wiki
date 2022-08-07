---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_AMENITIES_FROM_RELIGION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_AMENITIES_FROM_RELIGION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="ZEN_MEDITATION_AMENITY_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ZEN_MEDITATION_AMENITY_MODIFIER",
		"MODIFIER_SINGLE_CITY_ADJUST_CITY_AMENITIES_FROM_RELIGION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ZEN_MEDITATION_AMENITY_MODIFIER",
		"Amount",
		1
	);
	
```

