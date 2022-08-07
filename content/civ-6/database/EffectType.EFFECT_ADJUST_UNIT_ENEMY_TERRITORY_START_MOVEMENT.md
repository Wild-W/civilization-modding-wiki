---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ENEMY_TERRITORY_START_MOVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ENEMY_TERRITORY_START_MOVEMENT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="FUTURE_VICTORY_DOMINATION_ENEMY_TERRITORY_MOVEMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"FUTURE_VICTORY_DOMINATION_ENEMY_TERRITORY_MOVEMENT",
		"MODIFIER_PLAYER_UNITS_ADJUST_ENEMY_TERRITORY_START_MOVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FUTURE_VICTORY_DOMINATION_ENEMY_TERRITORY_MOVEMENT",
		"Amount",
		1
	);
	
```

