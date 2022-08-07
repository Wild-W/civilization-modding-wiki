---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_TRADE_ROUTE_PLUNDER_IMMUNITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_TRADE_ROUTE_PLUNDER_IMMUNITY
>
> * Class: `UNITS`
> * Parameters:
>	* DomainType `String`
>		* DOMAIN_AIR>		  DOMAIN_LAND>		  DOMAIN_SEA

## Samples

```SQL {title="TRADE_ROUTE_PLUNDER_IMMUNITY_SEA"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRADE_ROUTE_PLUNDER_IMMUNITY_SEA",
		"MODIFIER_PLAYER_UNIT_ADJUST_TRADE_ROUTE_PLUNDER_IMMUNITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRADE_ROUTE_PLUNDER_IMMUNITY_SEA",
		"DomainType",
		"DOMAIN_SEA"
	);
	
```

