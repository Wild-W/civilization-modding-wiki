---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_IDENTITY_PER_TURN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_IDENTITY_PER_TURN
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_ISIBONGO_GARRISONIDENTITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_ISIBONGO_GARRISONIDENTITY",
		"MODIFIER_PLAYER_CITIES_ADJUST_IDENTITY_PER_TURN",
		"CITY_HAS_GARRISON_UNIT_REQUIERMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ISIBONGO_GARRISONIDENTITY",
		"Amount",
		3
	);
	
```

