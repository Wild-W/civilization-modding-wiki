---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_EXTRA_ACCUMULATION_SPECIFIC_RESOURCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_EXTRA_ACCUMULATION_SPECIFIC_RESOURCE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* ResourceType `String`
>		* [Resources.ResourceType]

## Samples
```SQL {title="COMMEMORATION_AERONAUTICAL_GA_ALUMINUM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId
	)
VALUES
	(
		"COMMEMORATION_AERONAUTICAL_GA_ALUMINUM",
		"MODIFIER_PLAYER_CITIES_ADJUST_EXTRA_ACCUMULATION_SPECIFIC_RESOURCE",
		"PLAYER_HAS_GOLDEN_AGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COMMEMORATION_AERONAUTICAL_GA_ALUMINUM",
		"Amount",
		2
	),
	(
		"COMMEMORATION_AERONAUTICAL_GA_ALUMINUM",
		"ResourceType",
		"RESOURCE_ALUMINUM"
	);
	
```

