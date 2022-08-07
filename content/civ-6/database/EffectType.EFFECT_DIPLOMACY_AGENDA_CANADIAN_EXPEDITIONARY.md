---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_CANADIAN_EXPEDITIONARY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_CANADIAN_EXPEDITIONARY
>
> * Class: `PLAYERS`
> * Parameters:
>	* BottomPercentage `Integer`
>	* BottomRankingDiploMod `Integer`
>	* StatementKey `String`
>	* TopPercentage `Integer`
>	* TopRankingDiploMod `Integer`

## Samples

```SQL {title="AGENDA_CANADIAN_EXPEDITIONARY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_CANADIAN_EXPEDITIONARY",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_CANADIAN_EXPEDITIONARY",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_CANADIAN_EXPEDITIONARY",
		"BottomPercentage",
		30
	),
	(
		"AGENDA_CANADIAN_EXPEDITIONARY",
		"BottomRankingDiploMod",
		"-8"
	),
	(
		"AGENDA_CANADIAN_EXPEDITIONARY",
		"StatementKey",
		"AGENDA_CANADIAN_EXPEDITIONARY_WARNING"
	),
	(
		"AGENDA_CANADIAN_EXPEDITIONARY",
		"TopPercentage",
		65
	),
	(
		"AGENDA_CANADIAN_EXPEDITIONARY",
		"TopRankingDiploMod",
		8
	);
	
```

