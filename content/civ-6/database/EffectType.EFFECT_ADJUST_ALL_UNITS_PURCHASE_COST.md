---
tags:
- EffectType
title: EFFECT_ADJUST_ALL_UNITS_PURCHASE_COST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALL_UNITS_PURCHASE_COST
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* IncludeCivilian `Boolean`
>	* UnitDomain `String`
>		* DOMAIN_AIR>		  DOMAIN_LAND>		  DOMAIN_SEA

## Samples
```SQL {title="MINOR_CIV_CARTHAGE_BARRACKS_STABLE_PURCHASE_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"MINOR_CIV_CARTHAGE_BARRACKS_STABLE_PURCHASE_BONUS",
		"MODIFIER_PLAYER_CITIES_ADJUST_UNITS_PURCHASE_COST",
		"BUILDING_IS_BARRACKS_STABLE_MILITARITIC_CITY_STATE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_CARTHAGE_BARRACKS_STABLE_PURCHASE_BONUS",
		"Amount",
		20
	),
	(
		"MINOR_CIV_CARTHAGE_BARRACKS_STABLE_PURCHASE_BONUS",
		"UnitDomain",
		"DOMAIN_LAND"
	);
	
```

```SQL {title="SUGUBA_CHEAPER_UNIT_PURCHASE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SUGUBA_CHEAPER_UNIT_PURCHASE",
		"MODIFIER_SINGLE_CITY_ADJUST_ALL_UNITS_PURCHASE_COST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SUGUBA_CHEAPER_UNIT_PURCHASE",
		"Amount",
		20
	),
	(
		"SUGUBA_CHEAPER_UNIT_PURCHASE",
		"IncludeCivilian",
		1
	);
	
```

