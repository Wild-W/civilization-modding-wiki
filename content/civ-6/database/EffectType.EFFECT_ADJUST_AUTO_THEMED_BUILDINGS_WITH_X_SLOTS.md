---
tags:
- EffectType
title: EFFECT_ADJUST_AUTO_THEMED_BUILDINGS_WITH_X_SLOTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_AUTO_THEMED_BUILDINGS_WITH_X_SLOTS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`
>	* IsWonder `Boolean`

## Samples

```SQL {title="AUTO_THEME_AT_LEAST_3_SLOTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"AUTO_THEME_AT_LEAST_3_SLOTS",
		"MODIFIER_PLAYER_ADJUST_AUTO_THEME_BUILDINGS_WITH_X_SLOTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AUTO_THEME_AT_LEAST_3_SLOTS",
		"Amount",
		3
	),
	(
		"AUTO_THEME_AT_LEAST_3_SLOTS",
		"IsWonder",
		0
	);
	
```

