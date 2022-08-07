---
tags:
- EffectType
title: EFFECT_SETTLED_FOREIGN_CONTINENT_UNIT_CLASS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_SETTLED_FOREIGN_CONTINENT_UNIT_CLASS
>
> * Class: `Unknown`
> * Parameters:
>	* UnitPromotionClassType `String`

## Samples
```SQL {title="TRAIT_FOREIGN_CONTINENT_MELEE_UNIT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FOREIGN_CONTINENT_MELEE_UNIT",
		"MODIFIER_PLAYER_ADJUST_SETTLE_FOREIGN_CONTINENT_UNIT_CLASS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FOREIGN_CONTINENT_MELEE_UNIT",
		"UnitPromotionClassType",
		"PROMOTION_CLASS_MELEE"
	);
	
```

