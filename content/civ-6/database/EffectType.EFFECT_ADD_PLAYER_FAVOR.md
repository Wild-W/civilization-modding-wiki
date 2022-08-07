---
tags:
- EffectType
title: EFFECT_ADD_PLAYER_FAVOR
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_PLAYER_FAVOR
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="CIVIC_GRANT_FAVOR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CIVIC_GRANT_FAVOR",
		"MODIFIER_PLAYER_ADD_FAVOR"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CIVIC_GRANT_FAVOR",
		"Amount",
		50
	);
	
```

