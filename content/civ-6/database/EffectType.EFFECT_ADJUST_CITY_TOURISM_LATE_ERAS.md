---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_TOURISM_LATE_ERAS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_TOURISM_LATE_ERAS
>
> * Class: `CITIES`
> * Parameters:
>	* MinimumEra `String`
>		* [Eras.EraType]
>	* Modifier `Integer`

## Samples

```SQL {title="FILMSTUDIO_ENHANCEDLATETOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"FILMSTUDIO_ENHANCEDLATETOURISM",
		"MODIFIER_SINGLE_CITY_ADJUST_TOURISM_LATE_ERAS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FILMSTUDIO_ENHANCEDLATETOURISM",
		"MinimumEra",
		"ERA_MODERN"
	),
	(
		"FILMSTUDIO_ENHANCEDLATETOURISM",
		"Modifier",
		100
	);
	
```

