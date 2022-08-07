---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_AUTO_THEMED_BUILDING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_AUTO_THEMED_BUILDING
>
> * Class: `PLAYERS`
> * Parameters:
>	* BuildingType `String`
>		* [Buildings.BuildingType]

## Samples

```SQL {title="TRAIT_AUTO_THEME_ARCHAEOLOGY_MUSEUM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_AUTO_THEME_ARCHAEOLOGY_MUSEUM",
		"MODIFIER_PLAYER_ADJUST_AUTO_THEMED_BUILDING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_AUTO_THEME_ARCHAEOLOGY_MUSEUM",
		"BuildingType",
		"BUILDING_MUSEUM_ARTIFACT"
	);
	
```

