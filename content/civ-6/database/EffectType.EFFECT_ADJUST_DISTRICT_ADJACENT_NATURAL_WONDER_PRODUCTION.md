---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_ADJACENT_NATURAL_WONDER_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_ADJACENT_NATURAL_WONDER_PRODUCTION
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`
>	* FeatureType `String`

## Samples
```SQL {title="IKKIL_PRODUCTION_DISTRICT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId
	)
VALUES
	(
		"IKKIL_PRODUCTION_DISTRICT",
		"MODIFIER_ALL_CITIES_ADJUST_DISTRICT_ADJACENT_NATURAL_WONDER_PRODUCTION",
		"IKKIL_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"IKKIL_PRODUCTION_DISTRICT",
		"Amount",
		50
	),
	(
		"IKKIL_PRODUCTION_DISTRICT",
		"FeatureType",
		"FEATURE_IKKIL"
	);
	
```

