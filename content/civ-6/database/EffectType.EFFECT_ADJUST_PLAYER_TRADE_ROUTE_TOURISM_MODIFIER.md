---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_TOURISM_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_TOURISM_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GREATPERSON_TRADE_ROUTE_TOURISM_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_TRADE_ROUTE_TOURISM_MODIFIER",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_TOURISM_MODIFIER",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_TRADE_ROUTE_TOURISM_MODIFIER",
		"Amount",
		25
	);
	
```

