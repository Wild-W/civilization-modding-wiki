---
tags:
- EffectType
title: EFFECT_ADD_EXPENDED_GREAT_PERSON_TILES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_EXPENDED_GREAT_PERSON_TILES
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TRAIT_EXPENDED_GREAT_PERSON_TILES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_EXPENDED_GREAT_PERSON_TILES",
		"MODIFIER_PLAYER_CITIES_ADD_EXPENDED_GREAT_PERSON_TILES",
		"REQUIREMENTS_CITY_HAS_LAVRA"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_EXPENDED_GREAT_PERSON_TILES",
		"Amount",
		1
	);
	
```

