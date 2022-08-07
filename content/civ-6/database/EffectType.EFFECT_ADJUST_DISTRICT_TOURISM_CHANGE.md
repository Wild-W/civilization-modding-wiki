---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_TOURISM_CHANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_TOURISM_CHANGE
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="CONSERVATION_ANCIENT_WALL_TOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"CONSERVATION_ANCIENT_WALL_TOURISM",
		"MODIFIER_PLAYER_DISTRICTS_ADJUST_TOURISM_CHANGE",
		"DISTRICT_IS_CITY_CENTER_ANCIENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CONSERVATION_ANCIENT_WALL_TOURISM",
		"Amount",
		1
	);
	
```

