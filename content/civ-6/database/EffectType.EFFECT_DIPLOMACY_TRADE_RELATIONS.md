---
tags:
- EffectType
title: EFFECT_DIPLOMACY_TRADE_RELATIONS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_TRADE_RELATIONS
>
> * Class: `PLAYERS`
> * Parameters:
>	* BonusPerRoute `Boolean`
>	* NoTradePenalty `Integer`
>	* OnlyInboundTrade `Boolean`
>	* SimpleModifierDescription `String`
>	* StatementKey `String`
>	* TradeBonus `Integer`

## Samples

```SQL {title="AGENDA_BILLIONAIRE_TRADE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_BILLIONAIRE_TRADE",
		"MODIFIER_PLAYER_DIPLOMACY_TRADE_RELATIONS",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_30_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_BILLIONAIRE_TRADE",
		"BonusPerRoute",
		1
	),
	(
		"AGENDA_BILLIONAIRE_TRADE",
		"NoTradePenalty",
		12
	),
	(
		"AGENDA_BILLIONAIRE_TRADE",
		"OnlyInboundTrade",
		1
	),
	(
		"AGENDA_BILLIONAIRE_TRADE",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_WILHELMINA_BILLIONAIRE_TRADE"
	),
	(
		"AGENDA_BILLIONAIRE_TRADE",
		"StatementKey",
		"LOC_DIPLO_KUDO_LEADER_WILHELMINA_REASON_ANY"
	),
	(
		"AGENDA_BILLIONAIRE_TRADE",
		"TradeBonus",
		3
	);
	
```

