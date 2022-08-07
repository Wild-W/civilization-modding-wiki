---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_ALLOWED_IMPROVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_ALLOWED_IMPROVEMENT
>
> * Class: `CITIES`
> * Parameters:
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]

## Samples
```SQL {title="AQUACULTURE_CAN_BUILD_FISHERY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"AQUACULTURE_CAN_BUILD_FISHERY",
		"MODIFIER_CITY_ADJUST_ALLOWED_IMPROVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AQUACULTURE_CAN_BUILD_FISHERY",
		"ImprovementType",
		"IMPROVEMENT_FISHERY"
	);
	
```

