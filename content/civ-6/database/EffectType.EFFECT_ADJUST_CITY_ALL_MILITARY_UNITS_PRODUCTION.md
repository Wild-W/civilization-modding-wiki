---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_ALL_MILITARY_UNITS_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_ALL_MILITARY_UNITS_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* EndEra `String`
>		* [Eras.EraType]
>	* PromotionClass `String`
>		* [UnitPromotionClasses.PromotionClassType]
>	* StartEra `String`
>		* [Eras.EraType]

## Samples
```SQL {title="GOD_OF_THE_FORGE_UNIT_ANCIENT_CLASSICAL_PRODUCTION_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOD_OF_THE_FORGE_UNIT_ANCIENT_CLASSICAL_PRODUCTION_MODIFIER",
		"MODIFIER_PLAYER_CITIES_ADJUST_MILITARY_UNITS_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOD_OF_THE_FORGE_UNIT_ANCIENT_CLASSICAL_PRODUCTION_MODIFIER",
		"Amount",
		25
	),
	(
		"GOD_OF_THE_FORGE_UNIT_ANCIENT_CLASSICAL_PRODUCTION_MODIFIER",
		"EndEra",
		"ERA_CLASSICAL"
	),
	(
		"GOD_OF_THE_FORGE_UNIT_ANCIENT_CLASSICAL_PRODUCTION_MODIFIER",
		"StartEra",
		"ERA_ANCIENT"
	);
	
```

```SQL {title="GREATPERSON_CHESTER_NIMITZ_ACTIVE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		Permanent
	)
VALUES
	(
		"GREATPERSON_CHESTER_NIMITZ_ACTIVE",
		"MODIFIER_PLAYER_CITIES_ADJUST_MILITARY_UNITS_PRODUCTION",
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
		"GREATPERSON_CHESTER_NIMITZ_ACTIVE",
		"Amount",
		20
	),
	(
		"GREATPERSON_CHESTER_NIMITZ_ACTIVE",
		"PromotionClass",
		"PROMOTION_CLASS_NAVAL_RAIDER"
	);
	
```

