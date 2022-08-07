---
tags:
- EffectType
title: EFFECT_ALLIANCE_PRESSURE_FROM_NO_ALLY_RELIGION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ALLIANCE_PRESSURE_FROM_NO_ALLY_RELIGION
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="ALLIANCE_RELIGIOUS_PRESSURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ALLIANCE_RELIGIOUS_PRESSURE",
		"MODIFIER_ALLIANCE_PLAYERS_RELIGIOUS_PRESSURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALLIANCE_RELIGIOUS_PRESSURE",
		"Amount",
		20
	);
	
```

