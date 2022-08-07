---
tags:
- EffectType
title: EFFECT_CITY_GRANT_HERO
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_CITY_GRANT_HERO
>
> * Class: `Unknown`
> * Parameters:
>	* HeroClassType `Unknown`
>	* LocationBuildingType `Unknown`

## Samples
```SQL {title="MODIFIER_CREATE_HERO_ANANSI"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"MODIFIER_CREATE_HERO_ANANSI",
		"MODIFIER_CITY_GRANT_HERO",
		1,
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
		"MODIFIER_CREATE_HERO_ANANSI",
		"HeroClassType",
		"HEROCLASS_ANANSI"
	),
	(
		"MODIFIER_CREATE_HERO_ANANSI",
		"LocationBuildingType",
		"BUILDING_MONUMENT"
	);
	
```

