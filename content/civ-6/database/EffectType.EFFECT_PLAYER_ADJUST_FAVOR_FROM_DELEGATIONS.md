---
tags:
- EffectType
title: EFFECT_PLAYER_ADJUST_FAVOR_FROM_DELEGATIONS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_PLAYER_ADJUST_FAVOR_FROM_DELEGATIONS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples

```SQL {title="DIPLOMATIC_QUARTER_DELEGATION_FAVOR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DIPLOMATIC_QUARTER_DELEGATION_FAVOR",
		"MODIFIER_PLAYER_ADJUST_FAVOR_FROM_DELEGATIONS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DIPLOMATIC_QUARTER_DELEGATION_FAVOR",
		"Amount",
		1
	);
	
```
