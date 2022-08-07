---
tags:
- EffectType
title: EFFECT_ADJUST_BUILDING_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_BUILDING_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* BuildingType `String`
>		* [Buildings.BuildingType]
>	* DistrictType `String`
>		* [Districts.DistrictType]

## Samples

```SQL {title="MINOR_CIV_PRODUCTION_WALLS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_PRODUCTION_WALLS",
		"MODIFIER_PLAYER_CITIES_ADJUST_BUILDING_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_PRODUCTION_WALLS",
		"Amount",
		200
	),
	(
		"MINOR_CIV_PRODUCTION_WALLS",
		"BuildingType",
		"BUILDING_WALLS,BUILDING_CASTLE,BUILDING_STAR_FORT"
	);
	
```


```SQL {title="VETERANCY_ENCAMPMENT_BUILDINGS_PRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"VETERANCY_ENCAMPMENT_BUILDINGS_PRODUCTION",
		"MODIFIER_PLAYER_CITIES_ADJUST_BUILDING_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"VETERANCY_ENCAMPMENT_BUILDINGS_PRODUCTION",
		"Amount",
		30
	),
	(
		"VETERANCY_ENCAMPMENT_BUILDINGS_PRODUCTION",
		"DistrictType",
		"DISTRICT_ENCAMPMENT"
	);
	
```

