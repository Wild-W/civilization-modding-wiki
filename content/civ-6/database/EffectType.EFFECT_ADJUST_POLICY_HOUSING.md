---
tags:
- EffectType
title: EFFECT_ADJUST_POLICY_HOUSING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_POLICY_HOUSING
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="MONARCHY_WALLS_HOUSING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"MONARCHY_WALLS_HOUSING",
		"MODIFIER_PLAYER_CITIES_ADJUST_POLICY_HOUSING",
		"CITY_HAS_ANCIENT_WALLS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MONARCHY_WALLS_HOUSING",
		"Amount",
		1
	);
	
```

