---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_WITH_SHIELD_OR_ON_IT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_WITH_SHIELD_OR_ON_IT
>
> * Class: `PLAYERS`
> * Parameters:
>	* AvoidedWarPenalty `Integer`
>	* AvoidedWarPenaltyTurnsToRampUp `Integer`
>	* HighThreshold `Integer`
>	* IncrementValue `Integer`
>	* InitialValue `Integer`
>	* LowThreshold `Integer`
>	* MaxDiploModifierMagnitude `Integer`
>	* PaidForPeacePenalty `Boolean`
>	* PaidForPeacePenaltyTurnsToFadeOut `Integer`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`
>	* SimpleModifierDescription `String`
>	* StatementKey `String`

## Samples
```SQL {title="AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_WITH_SHIELD_OR_ON_IT",
		"ON_TURN_STARTED",
		"PLAYER_WITH_SHIELD_OR_ON_IT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"AvoidedWarPenalty",
		"-4"
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"AvoidedWarPenaltyTurnsToRampUp",
		15
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"HighThreshold",
		4
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"IncrementValue",
		0
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"InitialValue",
		0
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"LowThreshold",
		"-1"
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"MaxDiploModifierMagnitude",
		12
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"PaidForPeacePenalty",
		"-8"
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"PaidForPeacePenaltyTurnsToFadeOut",
		30
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"ReductionTurns",
		2
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"ReductionValue",
		0
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_WITH_SHIELD_OR_ON_IT"
	),
	(
		"AGENDA_MODIFIER_WITH_SHIELD_OR_ON_IT",
		"StatementKey",
		"LOC_DIPLO_WARNING_LEADER_GORGO_REASON_ANY"
	);
	
```

