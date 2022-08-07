---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_DISTRICT_AND_BUILDINGS_CREATE_UNIT_WITH_ABILITY_BY_CLASS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_DISTRICT_AND_BUILDINGS_CREATE_UNIT_WITH_ABILITY_BY_CLASS
>
> * Class: `PLAYERS`
> * Parameters:
>	* DistrictType `Unknown`
>	* UnitAbilityType `String`
>	* UnitPromotionClass `Unknown`

## Samples

```SQL {title="TRAIT_CREATE_HIPPODROME_HEAVY_CAVALRY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CREATE_HIPPODROME_HEAVY_CAVALRY",
		"MODIFIER_PLAYER_DISTRICT_ADJUST_PLAYER_DISTRICT_AND_BUILDINGS_CREATE_UNIT_WITH_ABILITY_BY_CLASS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CREATE_HIPPODROME_HEAVY_CAVALRY",
		"DistrictType",
		"DISTRICT_HIPPODROME"
	),
	(
		"TRAIT_CREATE_HIPPODROME_HEAVY_CAVALRY",
		"UnitAbilityType",
		"ABILITY_FREE_RESOURCE_MAITENANCE_HIPPODROME"
	),
	(
		"TRAIT_CREATE_HIPPODROME_HEAVY_CAVALRY",
		"UnitPromotionClass",
		"PROMOTION_CLASS_HEAVY_CAVALRY"
	);
	
```

