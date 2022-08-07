---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_TAG_ERA_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_TAG_ERA_PRODUCTION
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* EraType `String`
>		* [Eras.EraType]
>	* UnitPromotionClass `String`
>		* [UnitPromotionClasses.PromotionClassType]

## Samples
```SQL {title="TRAIT_ANCIENT_NAVAL_MELEE_PRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ANCIENT_NAVAL_MELEE_PRODUCTION",
		"MODIFIER_PLAYER_CITIES_ADJUST_UNIT_TAG_ERA_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ANCIENT_NAVAL_MELEE_PRODUCTION",
		"Amount",
		50
	),
	(
		"TRAIT_ANCIENT_NAVAL_MELEE_PRODUCTION",
		"EraType",
		"ERA_ANCIENT"
	),
	(
		"TRAIT_ANCIENT_NAVAL_MELEE_PRODUCTION",
		"UnitPromotionClass",
		"PROMOTION_CLASS_NAVAL_MELEE"
	);
	
```

