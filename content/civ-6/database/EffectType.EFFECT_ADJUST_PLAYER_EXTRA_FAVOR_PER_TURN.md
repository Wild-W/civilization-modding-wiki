---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_EXTRA_FAVOR_PER_TURN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_EXTRA_FAVOR_PER_TURN
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GOVCITYSTATES_ADJUST_FAVOR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOVCITYSTATES_ADJUST_FAVOR",
		"MODIFIER_PLAYER_ADJUST_EXTRA_FAVOR_PER_TURN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOVCITYSTATES_ADJUST_FAVOR",
		"Amount",
		3
	);
	
```

