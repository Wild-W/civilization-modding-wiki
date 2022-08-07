---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_CAPITAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_CAPITAL
>
> * Class: `PLAYERS`
> * Parameters:
>	* ProjectType `String`
>		* [Projects.ProjectType]

## Samples

```SQL {title="DISTRICT_COMPLETE_MOVE_CAPITAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DISTRICT_COMPLETE_MOVE_CAPITAL",
		"MODIFIER_PLAYER_ADJUST_CAPITAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DISTRICT_COMPLETE_MOVE_CAPITAL",
		"ProjectType",
		"PROJECT_COTHON_CAPITAL_MOVE"
	);
	
```

