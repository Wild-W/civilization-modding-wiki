---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_UNIT_PROJECT_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_UNIT_PROJECT_PERCENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GOV_PROJECT_ABILITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOV_PROJECT_ABILITY",
		"MODIFIER_PLAYER_ADJUST_UNIT_PROJECT_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOV_PROJECT_ABILITY",
		"Amount",
		2
	);
	
```

