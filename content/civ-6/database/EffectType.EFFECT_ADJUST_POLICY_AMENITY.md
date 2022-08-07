---
tags:
- EffectType
title: EFFECT_ADJUST_POLICY_AMENITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_POLICY_AMENITY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="LIBERALISM_SPECIALTYAMENITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"LIBERALISM_SPECIALTYAMENITY",
		"MODIFIER_PLAYER_CITIES_ADJUST_POLICY_AMENITY",
		"CITY_HAS_2_SPECIALTY_DISTRICTS_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"LIBERALISM_SPECIALTYAMENITY",
		"Amount",
		1
	);
	
```

