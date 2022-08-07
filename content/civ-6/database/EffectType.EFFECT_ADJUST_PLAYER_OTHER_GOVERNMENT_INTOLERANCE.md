---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_OTHER_GOVERNMENT_INTOLERANCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_OTHER_GOVERNMENT_INTOLERANCE
>
> * Class: `PLAYERS`
> * Parameters:
>	* IntoleranceMultiplier `Integer`
>	* SameEraIntoleranceFlatBonus `Integer`

## Samples

```SQL {title="AGENDA_ADJUST_GOVERNMENT_INTOLERANCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"AGENDA_ADJUST_GOVERNMENT_INTOLERANCE",
		"MODIFIER_PLAYER_GOVERNMENT_ADJUST_OTHER_GOVERNMENT_INTOLERANCE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_ADJUST_GOVERNMENT_INTOLERANCE",
		"IntoleranceMultiplier",
		2
	),
	(
		"AGENDA_ADJUST_GOVERNMENT_INTOLERANCE",
		"SameEraIntoleranceFlatBonus",
		"-6"
	);
	
```

