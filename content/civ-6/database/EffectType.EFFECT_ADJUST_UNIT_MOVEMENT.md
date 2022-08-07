---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_MOVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_MOVEMENT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="BERSERKER_FASTER_ENEMY_TERRITORY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"BERSERKER_FASTER_ENEMY_TERRITORY",
		"MODIFIER_PLAYER_UNIT_ADJUST_MOVEMENT",
		"BERSERKER_PLOT_IS_ENEMY_TERRITORY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BERSERKER_FASTER_ENEMY_TERRITORY",
		"Amount",
		2
	);
	
```

