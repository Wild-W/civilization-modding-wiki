---
tags:
- EffectType
title: EFFECT_ADOPT_ALLY_FOUNDED_RELIGIONS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADOPT_ALLY_FOUNDED_RELIGIONS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Adopt `Boolean`

## Samples

```SQL {title="MINOR_CIV_JERUSALEM_RELIGION_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_JERUSALEM_RELIGION_BONUS",
		"MODIFIER_PLAYER_ADOPT_ALLY_FOUNDED_RELIGIONS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_JERUSALEM_RELIGION_BONUS",
		"Adopt",
		1
	);
	
```

